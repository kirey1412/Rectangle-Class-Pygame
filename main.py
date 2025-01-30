import pgzrun, random, itertools

TITLE="Finding Mosquitos"
WIDTH=700
HEIGHT=700

torch_position=[(50,50), (650, 50), (650,650), (50,650)]
torch_pos = itertools.cycle(torch_position)

mosquito=Actor("mosquito", center=(50,50))
torch=Actor("torch", center=(WIDTH/2, HEIGHT/2))

def draw():
    screen.clear()
    torch.draw()
    mosquito.draw()

def movemosquito():
    animate(mosquito, "bounce_end", duration=1, pos=next(torch_pos))

movemosquito()
clock.schedule_interval(movemosquito, 2)

def movetorch():
    a=animate(torch, tween="linear", pos=torch.target, duration=torch.distance_to(torch.target)/200, on_finished=next_torch_target)

def next_torch_target():
    x=random.randint(100,600)
    y=random.randint(100,600)
    torch.target=x,y
    target_angle=torch.angle_to(torch.target)
    print(target_angle)
    target_angle+=360*((torch.angle-target_angle+180)//360)
    animate(torch, angle=target_angle, duration=0.3, on_finished=movetorch)
next_torch_target()
pgzrun.go()