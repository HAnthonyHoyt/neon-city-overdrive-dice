use itertools::Itertools;

const DICE_SIDES: usize = 6;
const SUCCESS_VALUE: usize = 4;
const MAX_SUCCESS_PERCENTAGE: f64 = 70.0;
const MAX_ACTION_DICE: usize = 6;

fn resolve_dice(action_roll: &mut Vec<usize>, danger_roll: &[usize]) {
    let sorted_danger_roll: Vec<usize> = danger_roll.iter().copied().sorted().collect();

    for &danger_die in sorted_danger_roll.iter() {
        if let Some(index) = action_roll.iter().position(|&die| die == danger_die) {
            action_roll.remove(index);
        }
    }
}

fn resolve_roll(action_roll: Vec<usize>, danger_roll: &[usize]) -> usize {
    let mut remaining_dice = action_roll.clone();
    resolve_dice(&mut remaining_dice, danger_roll);

    let top_result = remaining_dice.iter().copied().max().unwrap_or(0);
    top_result
}

fn is_success_roll(top_result: usize) -> bool {
    top_result >= SUCCESS_VALUE
}

fn get_dice_rolls(total_dice: usize) -> Vec<Vec<usize>> {
    if total_dice == 0 {
        return vec![vec![0]];
    }

    let mut combinations = Vec::new();
    dice_combinations_recursive(total_dice, &mut Vec::new(), &mut combinations);
    combinations
}

fn dice_combinations_recursive(
    remaining_dice: usize,
    current_combination: &mut Vec<usize>,
    combinations: &mut Vec<Vec<usize>>,
) {
    if remaining_dice == 0 {
        combinations.push(current_combination.clone());
        return;
    }

    for roll in 1..=DICE_SIDES {
        current_combination.push(roll);
        dice_combinations_recursive(remaining_dice - 1, current_combination, combinations);
        current_combination.pop();
    }
}

fn get_success_rate(action_total: usize, danger_total: usize) -> (f64, usize) {
    let action_rolls = get_dice_rolls(action_total);
    let danger_rolls = get_dice_rolls(danger_total);
    let mut success_rolls = 0;
    let mut total_rolls = 0;

    for action_roll in &action_rolls {
        for danger_roll in &danger_rolls {
            let top_result = resolve_roll(action_roll.clone(), danger_roll);
            let is_successful = is_success_roll(top_result);
            success_rolls += is_successful as usize;
            total_rolls += 1;
        }
    }

    let percent_success = (success_rolls as f64 / total_rolls as f64) * 100.0;
    (percent_success, total_rolls)
}

fn calculate_action_total(action_total: usize) -> Vec<String> {
    let mut action_results: Vec<String> = Vec::new();
    println!("Calculating for {} action dice", action_total);
    for danger_total in 0.. {
        println!("Calculating {} vs {}", action_total, danger_total);
        let (percent_success, total_tries) = get_success_rate(action_total, danger_total);
        let results = if percent_success > MAX_SUCCESS_PERCENTAGE {
            " - Good!"
        } else {
            ""
        };
        let result_string = format!(
            "{} vs {} - {:.0}% out of {:12} combinations{}",
            action_total, danger_total, percent_success, total_tries, results
        );
        action_results.push(result_string);
        if percent_success < MAX_SUCCESS_PERCENTAGE {
            // We stop calculating once we're past this value, so we can go on to the next action total
            break;
        }
    }
    println!("Done calculating for {} action dice", action_total);
    action_results
}

fn main() {
    println!(
        "Starting calculations, attempting all combinations for 1 to {} action dice",
        MAX_ACTION_DICE
    );
    println!("Results will take a long time to generate, please be patient");

    for action_dice in 1..=MAX_ACTION_DICE as usize {
        let dice_result = calculate_action_total(action_dice);
        println!("{}", dice_result.join("\n"));
    }
}
