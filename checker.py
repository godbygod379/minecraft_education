def on_on_chat():
    agent.teleport_to_player()

    for chessboard in range(4):
        odd_line()
        agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
        agent.turn(RIGHT_TURN)
        even_line()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 1)
    agent.turn(RIGHT_TURN)
    agent.move(UP, 1)


def odd_line():
    for i in range(4):
        agent.move(FORWARD, 1)
        agent.set_slot(1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.set_slot(2)
        agent.place(DOWN)

def even_line():
    for i in range(4):
        agent.set_slot(1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.set_slot(2)
        agent.place(DOWN)
        agent.move(FORWARD, 1)

def figure_odd_line():
    agent.move(FORWARD, 1)
    agent.set_slot(3)
    agent.place(DOWN)
    agent.move(FORWARD, 2)
    agent.place(DOWN)

player.on_chat("run", on_on_chat)
