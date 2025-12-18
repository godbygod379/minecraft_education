def on_on_chat():
    agent.teleport_to_player()
    def line1():
        
    for line3 in range(4):
        agent.move(FORWARD, 1)
        agent.set_slot(1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.set_slot(2)
        agent.place(DOWN)
player.on_chat("run", on_on_chat)
