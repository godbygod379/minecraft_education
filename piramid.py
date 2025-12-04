def on_on_chat():
    agent.teleport_to_player()
    agent.set_slot(1)
    for square in range(4):
        for side in range(9):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)
player.on_chat("run", on_on_chat)
