import toga
from toga.style.pack import COLUMN, Pack


def action_top_travel_icon(widget):
    print("amr")


def action_top_browser_icon(widget):
    print("browser")


def build(app):
    browser_icon = "icons/browser.png"
    plane_icon = "icons/plane.png"


    data = [
       # ('root%s' % i, 'value %s' % i)
       # for i in range(1, 100)
    ]

    left_container = toga.Table(headings=['Oracle Open', 'World'], data=data)

    right_content = toga.Box(
        style=Pack(direction=COLUMN, padding_top=50)
    )

    # for b in range(0, 10):
    #     right_content.add(
    #         toga.Button(
    #             'Oracle World - %s' % b,
    #             on_press=button_handler,
    #             style=Pack(width=200, padding=20)
    #         )
    #     )

    right_content.add (
        toga.Button(
            "Log In / Sign In",
            style=Pack(width=500,height=100, padding=20)
        )
    )

    right_content.add (
        toga.Button(
            "Oracle World Sessions",
            style=Pack(width=500,height=100, padding=20)
        )
    )

 
    right_container = toga.ScrollContainer(horizontal=False)

    right_container.content = right_content

    split = toga.SplitContainer()

    # The content of the split container can be specified as a simple list:
    #    split.content = [left_container, right_container]
    # but you can also specify "weight" with each content item, which will
    # set an initial size of the columns to make a "heavy" column wider than
    # a narrower one. In this example, the right container will be twice
    # as wide as the left one.
    split.content = [
        (left_container, 1),
        (right_container, 2)
    ]

    # Create a "Things" menu group to contain some of the commands.
    # No explicit ordering is provided on the group, so it will appear
    # after application-level menus, but *before* the Command group.
    # Items in the Things group are not explicitly ordered either, so they
    # will default to alphabetical ordering within the group.
    things = toga.Group('Things')
    top_travel_icon = toga.Command(
        action_top_travel_icon,
        label='Planner',
        tooltip='Plan Your Trip',
        icon=plane_icon,
        group=things
    )

    top_browser_icon = toga.Command(
        action_top_browser_icon,
        label='Browser',
        tooltip='Browser View',
        icon=browser_icon,
        group=things
    )
    

    # The order in which commands are added to the app or the toolbar won't
    # alter anything. Ordering is defined by the command definitions.
    app.commands.add(top_travel_icon, top_browser_icon)
    app.main_window.toolbar.add(top_travel_icon, top_browser_icon)

    return split


def main():
    return toga.App('OracleWorld2022', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()