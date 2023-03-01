step_forward = 2
step_backward = 1
distance = 10

total_step = 0

while distance > 0:
    total_step += step_forward
    distance -= step_forward

    if distance <= 0:
        break

    total_step += step_forward
    total_step += step_backward
    distance -= step_backward

print(f"The frog reached the target distance in {total_step} steps.")
