import numpy as np
import matplotlib.pyplot as plt

# Simulated aim data: list of (time, x, y) tuples
# For demonstration, this includes a natural aim and an aimbot-like aim
aim_data_natural = [
    (0, 100, 100), (1, 103, 105), (2, 108, 112), (3, 114, 121), (4, 122, 133)
]
aim_data_aimbot = [
    (0, 100, 100), (1, 200, 200), (2, 300, 300), (3, 250, 250), (4, 300, 300)
]

# Calculate velocity (change in position / change in time)
def calculate_velocity(aim_data):
    velocities = []
    for i in range(1, len(aim_data)):
        t1, x1, y1 = aim_data[i - 1]
        t2, x2, y2 = aim_data[i]
        dt = t2 - t1
        dx = x2 - x1
        dy = y2 - y1
        velocity = np.sqrt(dx**2 + dy**2) / dt
        velocities.append(velocity)
    return velocities

# Calculate jerkiness (sudden changes in velocity)
def calculate_jerkiness(velocities):
    jerkiness = []
    for i in range(1, len(velocities)):
        dv = velocities[i] - velocities[i - 1]
        jerkiness.append(abs(dv))
    return jerkiness

# Analyze aim data
natural_velocities = calculate_velocity(aim_data_natural)
natural_jerkiness = calculate_jerkiness(natural_velocities)

aimbot_velocities = calculate_velocity(aim_data_aimbot)
aimbot_jerkiness = calculate_jerkiness(aimbot_velocities)

# Plot results
plt.figure(figsize=(10, 6))

# Velocity comparison
plt.subplot(2, 1, 1)
plt.plot(natural_velocities, label="Natural Aim", marker="o")
plt.plot(aimbot_velocities, label="Aimbot", marker="o")
plt.title("Aim Velocity Comparison")
plt.ylabel("Velocity (pixels/sec)")
plt.legend()

# Jerkiness comparison
plt.subplot(2, 1, 2)
plt.plot(natural_jerkiness, label="Natural Aim", marker="o")
plt.plot(aimbot_jerkiness, label="Aimbot", marker="o")
plt.title("Aim Jerkiness Comparison")
plt.ylabel("Jerkiness (change in velocity)")
plt.xlabel("Frame Index")
plt.legend()

plt.tight_layout()
plt.show()
