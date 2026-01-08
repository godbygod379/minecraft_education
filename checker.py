def on_on_chat():
    agent.teleport_to_player()

    for chessboard in range(4):
        line1()
        agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
        agent.turn(RIGHT_TURN)
        line2()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)

def line1():
    for line3 in range(4):
        agent.move(FORWARD, 1)
        agent.set_slot(1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.set_slot(2)
        agent.place(DOWN)

def line2():
    for line4 in range(4):
        agent.set_slot(1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.set_slot(2)
        agent.place(DOWN)
        agent.move(FORWARD, 1)

player.on_chat("run", on_on_chat)
