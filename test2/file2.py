class assaytcell():
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    global client
    global run_id
    run_id = None

    def __init__(self, driver):
        self.driver = driver