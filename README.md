# Double-Pendulum-using-Lagrangian-Mechanics
I developed a double pendulum simulation using Lagrangian mechanics to derive coupled non-linear ODEs. With RK45 integration, it tracks four pendulums with nearly identical initial conditions. Even tiny differences (10⁻⁵ rad) cause trajectories to rapidly diverge, showcasing deterministic chaos.

Mathematical Model: The Double Pendulum

The double pendulum is a classic example of a nonlinear dynamical system exhibiting deterministic chaos. To model its motion, we use Lagrangian Mechanics, focusing on energy states rather than force vectors.

1. Generalized Coordinates
The system is defined by two angles, θ₁ and θ₂, measured from the vertical. The positions of the masses (m₁, m₂) are:
• Mass 1: x₁ = L₁ sin(θ₁), y₁ = -L₁ cos(θ₁)
• Mass 2: x₂ = x₁ + L₂ sin(θ₂), y₂ = y₁ - L₂ cos(θ₂)

2. Kinetic (T) & Potential (V) Energy
• T = ½m₁v₁² + ½m₂v₂²
• V = -(m₁ + m₂)gL₁ cos(θ₁) - m₂gL₂ cos(θ₂)

3. The Lagrangian & Equations of Motion
The Lagrangian is L = T - V. By applying the Euler-Lagrange Equation, we derive two coupled, non-linear second-order Ordinary Differential Equations (ODEs) for angular accelerations (where Δ = θ₁ - θ₂):

• θ̈₁ = [m₂g sin(θ₂) cos(Δ) - m₂ sin(Δ) (L₁θ̇₁² cos(Δ) + L₂θ̇₂²) - (m₁+m₂)g sin(θ₁)] / [L₁(m₁ + m₂ sin²(Δ))]
• θ̈₂ = [(m₁+m₂)(L₁θ̇₁² sin(Δ) - g sin(θ₂) + g sin(θ₁) cos(Δ)) + m₂L₂θ̇₂² sin(Δ) cos(Δ)] / [L₂(m₁ + m₂ sin²(Δ))]

4. Numerical Solution
Since no analytical solution exists, we reduce the system to four first-order ODEs: y = [θ₁, θ̇₁, θ₂, θ̇₂]. We solve this using the RK45 algorithm (Explicit Runge-Kutta). This captures the "Butterfly Effect"—where a tiny difference of just 10⁻⁵ radians causes the paths to diverge into completely unique trajectories.
