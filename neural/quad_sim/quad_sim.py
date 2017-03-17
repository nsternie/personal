import quad

q = quad.Quadcopter('quad.config')

#q.print_variables()

t = [50,50,50,50]

q.set_throttle(t)

print q.thrust
q.step()
print q.thrust
