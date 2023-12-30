import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model_2_body_problem(state, t):
    gravitational_parameter = 3.248E+05
    x = state[0]
    y = state[1]
    z = state[2]
    x_velocity = state[3]
    y_velocity = state[4]
    z_velocity = state[5]
    x_acceleration = -gravitational_parameter * x / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    y_acceleration = -gravitational_parameter * y / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    z_acceleration = -gravitational_parameter * z / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    dstate_dt = [x_velocity, y_velocity, z_velocity, x_acceleration, y_acceleration, z_acceleration]
    return dstate_dt
  
# Начальные положения
satellite_initial_x = -30000
satellite_initial_y = -55000
satellite_initial_z = 12000
satellite_initial_velocity_x = 1
satellite_initial_velocity_y = 0.8
satellite_initial_velocity_z = 0.5
state_0 = [satellite_initial_x, satellite_initial_y, satellite_initial_z,
           satellite_initial_velocity_x, satellite_initial_velocity_y, satellite_initial_velocity_z]

time = np.linspace(0, 36 * 3600, 200)

solution = odeint(model_2_body_problem, state_0, time)
satellite_x = solution[:, 0]
satellite_y = solution[:, 1]
satellite_z = solution[:, 2]

num_points = 50
phi = np.linspace(0, 2 * np.pi, num_points)
theta = np.linspace(0, np.pi, num_points)
theta, phi = np.meshgrid(theta, phi)

jool_radius = 6000  # Радиус планеты Jool
jool_x = jool_radius * np.cos(phi) * np.sin(theta)
jool_y = jool_radius * np.sin(phi) * np.sin(theta)
jool_z = jool_radius * np.cos(theta)

fig = plt.figure()
axes = fig.add_subplot(111, projection='3d')
axes.plot_surface(jool_x, jool_y, jool_z, color='green', alpha=0.7)
axes.plot3D(satellite_x, satellite_y, satellite_z, 'purple')
axes.view_init(25, 145)
axes.set_title('Задача двух тел')
axes.set_xlabel('X km')
axes.set_ylabel('Y km')
axes.set_zlabel('Z km')
plt.show()
