def on_on_chat(hi):
    agent.teleport(pos(0, 10, 0), WEST)
    agent.set_slot(1)
    while hi > 0:
        for square in range(4):
            for side in range(0, hi):
                agent.place(DOWN)
                agent.move(FORWARD, 1)
            agent.turn(LEFT_TURN)
        agent.move(LEFT, 1)
        agent.move(UP, 1)
        agent.move(FORWARD, 1)
        hi = hi - 2
player.on_chat("run", on_on_chat)
