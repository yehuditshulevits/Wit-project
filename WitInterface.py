from Wit import *


class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        match command:
            case "init":
                Wit.init()
            case "add":
                Wit.add(args)
            case "commit":
                Wit.commit()
            case _:
                raise Exception("Sorry, your request is wrong")
