import numpy as np
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from scipy.integrate import solve_ivp

# ----------------------------
# Physical constants
# ----------------------------
g = 9.81
L1, L2 = 1.0, 1.0
m1, m2 = 1.0, 1.0

def equations(t, y):
    th1, w1, th2, w2 = y
    c, s = np.cos(th1-th2), np.sin(th1-th2)

    return [
        w1,
        (m2*g*np.sin(th2)*c
         - m2*s*(L1*w1**2*c + L2*w2**2)
         - (m1+m2)*g*np.sin(th1)) / (L1*(m1 + m2*s**2)),
        w2,
        ((m1+m2)*(L1*w1**2*s
         - g*np.sin(th2)
         + g*np.sin(th1)*c)
         + m2*L2*w2**2*s*c) / (L2*(m1 + m2*s**2))
    ]

# ----------------------------
# Time
# ----------------------------
t_span = (0, 10)
t_eval = np.linspace(*t_span, 1200)

initial_conditions = [
    [np.pi/2, 0, np.pi/2, 0],
    [np.pi/2 + 1e-5, 0, np.pi/2, 0],
    [np.pi, 0, np.pi/2, 0],
    [np.pi/3, 0, np.pi/2, 0],
]

solutions = [solve_ivp(equations, t_span, ic, t_eval=t_eval)
             for ic in initial_conditions]

# ----------------------------
# Figure
# ----------------------------
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.axis("off")

colors = ["tab:blue", "tab:red", "tab:green", "tab:purple"]

# Rods
rods = []
# End bubbles
bubbles = []
# Trails
trails = []

for c in colors:
    rod, = ax.plot([], [], lw=2, color=c)
    bubble, = ax.plot([], [], "o", color=c, markersize=6)
    trail, = ax.plot([], [], lw=1, color=c, alpha=0.7)

    rods.append(rod)
    bubbles.append(bubble)
    trails.append(trail)

# Path memory
path_x = [[] for _ in initial_conditions]
path_y = [[] for _ in initial_conditions]

# ----------------------------
# Animation
# ----------------------------
def animate(i):
    for k, sol in enumerate(solutions):
        th1, th2 = sol.y[0][i], sol.y[2][i]

        x1 = L1*np.sin(th1)
        y1 = -L1*np.cos(th1)
        x2 = x1 + L2*np.sin(th2)
        y2 = y1 - L2*np.cos(th2)

        rods[k].set_data([0, x1, x2], [0, y1, y2])

        # FIX: scalar → sequence
        bubbles[k].set_data([x2], [y2])

        path_x[k].append(x2)
        path_y[k].append(y2)
        trails[k].set_data(path_x[k], path_y[k])

    return rods + bubbles + trails

ani = FuncAnimation(
    fig,
    animate,
    frames=len(t_eval),
    interval=20,
    blit=True
)

# ----------------------------
# Save MP4
# ----------------------------
writer = FFMpegWriter(fps=30, bitrate=2000)
ani.save("aaaa.mp4", writer=writer)

plt.close(fig)
print("Saved: double_pendulum_chaos_bubbles_paths.mp4")
