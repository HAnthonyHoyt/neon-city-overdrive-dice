const DICE_SIDES: i32 = 6;
const SUCCESS_VALUE: i32 = DICE_SIDES / 2 + 1;
const MAX_SUCCESS_PERC: i32 = 70;
const MAX_ACTION_DICE: usize = 6;

fn resolve_dice(mut action_roll: Vec<i32>, danger_roll: &[i32]) -> Vec<i32> {
    let mut sorted_danger_roll: Vec<i32> = danger_roll.to_vec();
    sorted_danger_roll.sort();

    for &danger_die in sorted_danger_roll.iter() {
        if let Some(index) = action_roll.iter().position(|&die| die == danger_die) {
            action_roll.remove(index);
        }
    }
    action_roll
}

fn resolve_roll(action_roll: Vec<i32>, danger_roll: &[i32]) -> i32 {
    let remaining_dice = resolve_dice(action_roll, danger_roll);
    let top_result = remaining_dice.iter().copied().max().unwrap_or(0);
    top_result
}

fn is_success_roll(top_result: i32) -> bool {
    top_result >= SUCCESS_VALUE
}

fn main() {
    let action_roll: Vec<i32> = vec![1, 2, 3, 4, 5];
    let danger_roll: Vec<i32> = vec![3, 4];

    let top_result = resolve_roll(action_roll, &danger_roll);
    let is_success = is_success_roll(top_result);

    println!("Top result: {}", top_result);
    println!("Is success roll: {}", is_success);
}
