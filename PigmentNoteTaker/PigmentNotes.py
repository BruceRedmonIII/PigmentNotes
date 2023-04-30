import re
import wx

# My pigment dictionary will help me dynamically call on different pigment codes
pigment_names = {}

config_file = open('config.txt', 'r+')
config_lines = config_file.readlines()


# This is the window that displays when called
# I use super since it's technically a subclass of what is defined in wx already


class PigmentNoteWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Pigment Notes", size=(500, 200))

        config_notebook_color = re.compile(r'(?<=Notebook Color = )(.*)')

        self.set_color = "None"
        # I have this incase I want to make a config file later, this would be where I set the values
        for index, line in enumerate(config_lines):
            if "config" in line:
                for word in line.split('.'):
                    if word.find("config") != -1:
                        try:
                            search = config_notebook_color.search(line)
                            self.set_color = search.group()
                            print(search.group())
                        except AttributeError as e:
                            print("Error:", e)

        notebook = wx.Notebook(self, size=(260, 160), pos=(0, 0))
        notebook.SetBackgroundColour(self.set_color)
        # This is the find code panel, it includes the button "Find" and then calls the function when clicked
        find_panel = wx.Panel(notebook)
        self.find_text = wx.TextCtrl(find_panel, pos=(0, 30))
        self.find_button = wx.Button(find_panel, label="Find", size=(110, 30))
        self.find_button.Bind(wx.EVT_BUTTON, self.on_find_button_click)
        # This is the create_panel where I set each panel to fill in when creating a code
        create_panel = wx.Panel(notebook)
        self.save_button = wx.Button(create_panel, label="Save", size=(110, 30))
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save_button_click)
        self.code_text_static = wx.StaticText(create_panel, pos=(0, 30), label="Code")
        self.code_text = wx.TextCtrl(create_panel, pos=(30, 30), size=(78, 20))
        self.color_text_static = wx.StaticText(create_panel, pos=(0, 50), label="Color")
        self.color_text = wx.TextCtrl(create_panel, pos=(30, 50), size=(78, 20))
        self.wash_text_static = wx.StaticText(create_panel, pos=(0, 70), label="Wash")
        self.wash_text = wx.TextCtrl(create_panel, pos=(30, 70), size=(78, 20))
        self.skids_text_static = wx.StaticText(create_panel, pos=(0, 90), label="Skids")
        self.skids_text = wx.TextCtrl(create_panel, pos=(30, 90), size=(78, 20))
        self.bags_text_static = wx.StaticText(create_panel, pos=(0, 110), label="Bags")
        self.bags_text = wx.TextCtrl(create_panel, pos=(30, 110), size=(78, 20))
        self.tags_text_static = wx.StaticText(create_panel, pos=(120, 0), label="Tags")
        self.tags_text = wx.TextCtrl(create_panel, pos=(155, 0), size=(78, 20))
        self.pump_text_static = wx.StaticText(create_panel, pos=(120, 20), label="Pump")
        self.pump_text = wx.TextCtrl(create_panel, pos=(155, 20), size=(78, 20))
        self.drain_text_static = wx.StaticText(create_panel, pos=(120, 40), label="Drain")
        self.drain_text = wx.TextCtrl(create_panel, pos=(155, 40), size=(78, 20))
        self.comment_text_static = wx.StaticText(create_panel, pos=(120, 60), label="Comments")
        self.comment_text = wx.TextCtrl(create_panel, pos=(120, 80), size=(128, 50))
        # This is the edit_panel where I used alot of the same code as create_panel,
        # but specified they are part of the edit panel instead
        edit_panel = wx.Panel(notebook)
        self.edit_button = wx.Button(edit_panel, label="Edit", size=(110, 30))
        self.edit_button.Bind(wx.EVT_BUTTON, self.on_edit_button_click)
        self.edit_code_text_static = wx.StaticText(edit_panel, pos=(0, 30), label="Code")
        self.edit_code_text = wx.TextCtrl(edit_panel, pos=(30, 30), size=(78, 20))
        self.edit_color_text_static = wx.StaticText(edit_panel, pos=(0, 50), label="Color")
        self.edit_color_text = wx.TextCtrl(edit_panel, pos=(30, 50), size=(78, 20))
        self.edit_wash_text_static = wx.StaticText(edit_panel, pos=(0, 70), label="Wash")
        self.edit_wash_text = wx.TextCtrl(edit_panel, pos=(30, 70), size=(78, 20))
        self.edit_skids_text_static = wx.StaticText(edit_panel, pos=(0, 90), label="Skids")
        self.edit_skids_text = wx.TextCtrl(edit_panel, pos=(30, 90), size=(78, 20))
        self.edit_bags_text_static = wx.StaticText(edit_panel, pos=(0, 110), label="Bags")
        self.edit_bags_text = wx.TextCtrl(edit_panel, pos=(30, 110), size=(78, 20))
        self.edit_tags_text_static = wx.StaticText(edit_panel, pos=(120, 0), label="Tags")
        self.edit_tags_text = wx.TextCtrl(edit_panel, pos=(155, 0), size=(78, 20))
        self.edit_pump_text_static = wx.StaticText(edit_panel, pos=(120, 20), label="Pump")
        self.edit_pump_text = wx.TextCtrl(edit_panel, pos=(155, 20), size=(78, 20))
        self.edit_drain_text_static = wx.StaticText(edit_panel, pos=(120, 40), label="Drain")
        self.edit_drain_text = wx.TextCtrl(edit_panel, pos=(155, 40), size=(78, 20))
        self.edit_comment_text_static = wx.StaticText(edit_panel, pos=(120, 60), label="Comments")
        self.edit_comment_text = wx.TextCtrl(edit_panel, pos=(120, 80), size=(128, 50))
        # The basic notebook setters
        notebook.AddPage(find_panel, "Find")
        notebook.AddPage(create_panel, "Create")
        notebook.AddPage(edit_panel, "Edit")
        # I create the info panel here along with the info message which will display whatever it is set to
        # I also gave it 2 styles, 1 being read only, and the other being multiLine
        info_panel = wx.Panel(self, size=(200, 150))
        self.info_message = wx.TextCtrl(info_panel, style=wx.TE_READONLY | wx.TE_MULTILINE, size=(200, 150))
        info_panel.SetPosition((280, 0))

        self.Show()

    def on_find_button_click(self, event):
        value = self.find_text.GetValue()
        pigment_found = pigment_names[value].display_pigment_info()
        self.info_message.SetValue(pigment_found)

        pass

    def on_save_button_click(self, event):
        # This starts by taking the values of each text box
        code_value = self.code_text.GetValue()
        color_value = self.color_text.GetValue()
        wash_value = self.wash_text.GetValue()
        skids_value = self.skids_text.GetValue()
        bags_value = self.bags_text.GetValue()
        tags_value = self.tags_text.GetValue()
        pump_value = self.pump_text.GetValue()
        drain_value = self.drain_text.GetValue()
        comments_value = self.comment_text.GetValue()
        # It then checks to make sure that the code isn't blank, as we need that for finding the code
        # It also checks to see if the code already exists, in which it will display that it exists
        # If everything passes, then it will create the new pigment class, and then save it to the file
        if code_value != "" and pigment_names.get(code_value) is None:
            pigment_names[code_value] = Pigment(code_value, color_value, wash_value,
                                                skids_value, bags_value, tags_value,
                                                pump_value, drain_value,
                                                comments_value)
            pigment_names[code_value].save_pigment_code()
            save_all_pigment_classes()
            message = pigment_names[code_value].display_pigment_info()
        elif code_value == "":
            message = "Must enter a code!"
        elif pigment_names.get(code_value) is not None:
            message = "Code already exists!"
        else:
            message = "idk man"

        self.info_message.SetValue(message)

        pass

    def on_edit_button_click(self, event):
        # This checks to make sure there is a code in the code box before trying to edit anything
        if self.edit_code_text.GetValue() == "":
            pigment_found = "Must enter a code to search!"
        else:
            # It starts with a bunch of checks to see if that value has been changed in the box, if the box is blank
            # It won't update the value to be blank
            if self.edit_color_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].color = self.edit_color_text.GetValue()
            if self.edit_wash_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].wash_time = self.edit_wash_text.GetValue()
            if self.edit_skids_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].skids = self.edit_skids_text.GetValue()
            if self.edit_bags_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].bags = self.edit_bags_text.GetValue()
            if self.edit_tags_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].tags = self.edit_tags_text.GetValue()
            if self.edit_pump_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].pumping_time = self.edit_pump_text.GetValue()
            if self.edit_drain_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].drain_time = self.edit_drain_text.GetValue()
            if self.edit_comment_text.GetValue() != "":
                pigment_names[self.edit_code_text.GetValue()].comments = self.edit_comment_text.GetValue()
                # After all the checks and updates have been set, it will display it in the info box
                # And update the code
            pigment_found = pigment_names[self.edit_code_text.GetValue()].display_pigment_info()
            pigment_names[self.edit_code_text.GetValue()].update_pigment_code()
            save_all_pigment_classes()

        self.info_message.SetValue(pigment_found)

        pass


class Pigment:
    def __init__(self, code, color, wash_time, skids, bags, tags, pumping_time, drain_time, comments):
        self.code = code
        self.color = color
        self.wash_time = wash_time
        self.skids = skids
        self.bags = bags
        self.tags = tags
        self.pumping_time = pumping_time
        self.drain_time = drain_time
        self.comments = comments
        # The nice thing about using a UI is that I can now cloud the console with information like this
        # that would normally make the code harder to use
        print(f"{self.code} pigment created")

    def get_code(self):
        return self.code

    def get_color(self):
        return self.color

    def get_wash_time(self):
        return self.wash_time

    def get_sales(self):
        return self.skids

    def get_cages(self):
        return self.bags

    def get_direct_ship(self):
        return self.tags

    def get_pumping_time(self):
        return self.pumping_time

    def get_drain_time(self):
        return self.drain_time

    def get_comments(self):
        return self.comments

    def save_pigment_code(self):
        # This is for individually saving the code
        save_file.write("\n Code = " + self.code + " Color = " + self.color)
        save_file.write(" Wash Time = " + self.wash_time + " Skids = " + self.skids)
        save_file.write(" Bag Type = " + self.bags + " Direct Ship = " + self.tags)
        save_file.write(" Pumping Time = " + self.pumping_time + " Drain Time = " + self.drain_time)
        save_file.write(" Comments = " + self.comments + "\n")
        print(f"{self.code} Saved Successfully")

    def update_pigment_code(self):
        for index, line in enumerate(lines):
            if self.code in line:
                try:
                    # re.sub lets me specify the exact location of what I want to change
                    # and line = is used to actually change the text file
                    line = re.sub(r'(?<=Color = )(.*)(?= Wash Time)', self.color, line)
                    line = re.sub(r'(?<=Wash Time = )(.*)(?= Skids)', self.wash_time, line)
                    line = re.sub(r'(?<=Skids = )(.*)(?= Bag Type)', self.skids, line)
                    line = re.sub(r'(?<=Bag Type = )(.*)(?= Direct Ship)', self.bags, line)
                    line = re.sub(r'(?<=Direct Ship = )(.*)(?= Pumping Time)', self.tags, line)
                    line = re.sub(r'(?<=Pumping Time = )(.*)(?= Drain Time)', self.pumping_time, line)
                    line = re.sub(r'(?<=Drain Time = )(.*)(?= Comments)', self.drain_time, line)
                    line = re.sub(r'(?<=Comments = )(.*)', self.comments, line)
                    # If I try to save again it will tell me that the code already exists
                    # because of the safety net, I have to manually save this, or have to redo my safe function
                    # This will start by taking the line that the code was found on, moving the pointer to
                    # the start of the line, and then deleting it, followed by rewriting that line with
                    # the new values
                    lines[index] = line
                    save_file.seek(0)
                    save_file.truncate()
                    save_file.writelines(lines)
                except AttributeError as e:
                    print("Error:", e)

    def display_pigment_info(self):
        # This will start by creating a string variable
        # And then adding to it with all the lines of code below
        # It returns the final result, I can then display it on my UI
        show_this = ""
        show_this += f"Code = {self.code}"
        show_this += f"\nColor = {self.color}"
        show_this += f"\nWash Time = {self.wash_time}"
        show_this += f"\nSkids = {self.skids}"
        show_this += f"\nBags = {self.bags}"
        show_this += f"\nTags = {self.tags}"
        show_this += f"\nPumping Time = {self.pumping_time}"
        show_this += f"\nDrain Time = {self.drain_time}"
        show_this += f"\nComments = {self.comments}"
        return show_this


"""""
    def edit_pigment_code(self):
        # This entire code can be ignored, it was before I had my UI
        # The only reason I'm keeping this in is so I have very basic controls outside the UI
        # as I just started using UI, and might need to troubleshoot code later
        # for now it will be commented out for loading speed
        print("What are we changing?\n"
              "1 for color\n"
              "2 for wash time\n"
              "3 for skids\n"
              "4 for bags\n"
              "5 for tags\n"
              "6 for pumping estimate\n"
              "7 for draining time\n"
              "8 for comments")
        loop = True
        while loop:
            user_input = input()
            if user_input == "1":
                print("Enter new color")
                new_input = input()
                self.color = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "2":
                print("Enter new Wash Time")
                new_input = input()
                self.wash_time = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "3":
                print("Enter new type of skids")
                new_input = input()
                self.skids = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "4":
                print("Enter new bags")
                new_input = input()
                self.bags = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "5":
                print("Enter new tag placement")
                new_input = input()
                self.tags = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "6":
                print("Enter new Pumping Time")
                new_input = input()
                self.pumping_time = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "7":
                print("Enter new Drain Time")
                new_input = input()
                self.drain_time = str(new_input)
                self.update_pigment_code()
                return
            elif user_input == "8":
                print("Enter new Comments")
                new_input = input()
                self.comments = str(new_input)
                self.update_pigment_code()
                return
"""


def check_for_duplicates(code):
    # This will check all lines for the code you specify as the argument
    for index, line in enumerate(lines):
        if code in line:
            for word in line.split('.'):
                if word.find(code) != -1:
                    return True

    return False


def save_all_pigment_classes():
    # This is my save all function where I can save the entire script at once
    # It also keeps an index of what line I'm on incase there is an error
    # An idea I had when some lines would have issues earlier in the making of this program
    for index, line in enumerate(lines):
        if "Code" in line:
            for word in line.split('.'):
                if word.find("Code") != -1:
                    try:
                        search = class_gather_code.search(line)
                        if not check_for_duplicates(search.group()):
                            pigment_names[search.group()].save_pigment_code()
                            # I commented this out due to it finding a duplicate every save, seemed redundant
#                        else:
#                            print('duplicate found in trying to save')
                    except AttributeError as e:
                        print(f"Error Line {index}: ", e)


def create_pigment_classes():
    # This is the bread and butter of the program, it starts by looking for the
    # keyword "Code" That all pigment saves have. It then sets each value of the text, to a variable
    # and then shortens it by using the .group() syntax.
    # Finally, if that code hasn't already been created into a class, it will then create the class
    # starting with setting the dictionary to the code
    for index, line in enumerate(lines):
        if "Code" in line:
            for word in line.split('.'):
                if word.find("Code") != -1:
                    try:
                        search = class_gather_code.search(line)
                        search2 = class_gather_color.search(line)
                        search3 = class_gather_wash_time.search(line)
                        search4 = class_gather_skids.search(line)
                        search5 = class_gather_bags.search(line)
                        search6 = class_gather_direct_ship.search(line)
                        search7 = class_gather_pumping_time.search(line)
                        search8 = class_gather_drain_time.search(line)
                        search9 = class_gather_comments.search(line)
                        code = search.group()
                        color = search2.group()
                        wash_time = search3.group()
                        sales = search4.group()
                        cages = search5.group()
                        direct_ship = search6.group()
                        pumping_time = search7.group()
                        drain_time = search8.group()
                        comments = search9.group()
                        if code not in pigment_names:
                            pigment_names[code] = Pigment(code, color, wash_time,
                                                          sales, cages,
                                                          direct_ship, pumping_time,
                                                          drain_time, comments)
                        else:
                            print(f"{code} Duplicate found!")
                    except AttributeError as e:
                        print("Error:", e)


"""
def new_pigment_code():
    # This is again left over code from before the UI
    print('enter code')
    code = input()
    print('enter color')
    color = input()
    print('enter Wash Time')
    wash = input()
    print('enter skids')
    skids = input()
    print('enter bags')
    bags = input()
    print('enter tags')
    tags = input()
    print('enter Pumping Time')
    pumping = input()
    print('enter Drain Time')
    drain = input()
    print('enter comments')
    comments = input()
    pigment_names[code] = Pigment(code, color, wash, skids, bags, tags, pumping, drain, comments)
    pigment_names[code].save_pigment_code()
"""


def find_pigment_code(code):
    # This starts by creating a string variable, and then adding to it
    # by using the different variables of the class it found
    show_this = ""
    for index, line in enumerate(lines):
        if code in line:
            for word in line.split('.'):
                if word.find(code) != -1:
                    try:
                        search = gather_code.search(line)
                        show_this += (search.group())
                        show_this += "\n"
                        search2 = gather_color.search(line)
                        show_this += (search2.group())
                        show_this += "\n"
                        search3 = gather_wash_time.search(line)
                        show_this += (search3.group())
                        show_this += "\n"
                        search4 = gather_skids.search(line)
                        show_this += (search4.group())
                        show_this += "\n"
                        search5 = gather_bags.search(line)
                        show_this += (search5.group())
                        show_this += "\n"
                        search6 = gather_direct_ship.search(line)
                        show_this += (search6.group())
                        show_this += "\n"
                        search7 = gather_pumping_time.search(line)
                        show_this += (search7.group())
                        show_this += "\n"
                        search8 = gather_drain_time.search(line)
                        show_this += (search8.group())
                        show_this += "\n"
                        search9 = gather_comments.search(line)
                        show_this += (search9.group())
                        show_this += "\n"
                    except AttributeError as e:
                        print("Error:", e)
    return show_this


# This will be used to default the entire file if there is a big issue that needs fixed.
def restart_all_notes():
    with open("PigmentSavefile.txt", "w") as the_save_file, open('DefaultSaveFile.txt', 'r') as default_file:
        for line in default_file:
            the_save_file.write(line)


# All of my re is written here
gather_code = re.compile(r'Code = (.*)(?= Color)')
gather_color = re.compile(r'Color = (.*)(?= Wash Time)')
gather_wash_time = re.compile(r'Wash Time = (.*)(?= Skids)')
gather_skids = re.compile(r'Skids = (.*)(?= Bag Type)')
gather_bags = re.compile(r'Bag Type = (.*)(?= Direct Ship)')
gather_direct_ship = re.compile(r'Direct Ship = (.*)(?= Pumping Time)')
gather_pumping_time = re.compile(r'Pumping Time = (.*)(?= Drain Time)')
gather_drain_time = re.compile(r'Drain Time = (.*)(?= Comments)')
gather_comments = re.compile(r'Comments = (.*)')

class_gather_code = re.compile(r'(?<=Code = )(.*)(?= Color)')
class_gather_color = re.compile(r'(?<=Color = )(.*)(?= Wash Time)')
class_gather_wash_time = re.compile(r'(?<=Wash Time = )(.*)(?= Skids)')
class_gather_skids = re.compile(r'(?<=Skids = )(.*)(?= Bag Type)')
class_gather_bags = re.compile(r'(?<=Bag Type = )(.*)(?= Direct Ship)')
class_gather_direct_ship = re.compile(r'(?<=Direct Ship = )(.*)(?= Pumping Time)')
class_gather_pumping_time = re.compile(r'(?<=Pumping Time = )(.*)(?= Drain Time)')
class_gather_drain_time = re.compile(r'(?<=Drain Time = )(.*)(?= Comments)')
class_gather_comments = re.compile(r'(?<=Comments = )(.*)')

# Finally we will close the config file as the UI has been created, and then open the save file
# for all the pigment codes
config_file.close()
save_file = open("PigmentSavefile.txt", "r+")
lines = save_file.readlines()
create_pigment_classes()

# We create the application, then create the pigment window with the given name
# and then show the window
app = wx.App()
pigment_window = PigmentNoteWindow()
pigment_window.Show()
app.MainLoop()

# while game_loop:
#    print("Type 'q' to quit, or 'y' to search another code, press 'e' to edit this code, or press 'n' for new code")
#    user_menu_choice = input()
#    if user_menu_choice == "q":
#        game_loop = False
#    elif user_menu_choice == "y":
#        print("what code would you like to search?")
#        user_code = str(input())
#        find_pigment_code(user_code)
#    elif user_menu_choice == "e":
#        print("what code would you like to edit?")
#        user_code = str(input())
#        pigment_names[user_code].edit_pigment_code()
#        save_all_pigment_classes()
#    elif user_menu_choice == "n":
#        new_pigment_code()
#        save_all_pigment_classes()

save_all_pigment_classes()

save_file.close()
