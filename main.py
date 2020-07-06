from pysine import sine
import random


chromatic_scale = [440.00, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61]
pentatonic_scale = [440.00, 523.25, 587.33, 659.25, 783.99]
blues_scale = [440.00, 523.25, 587.33, 622.25, 659.25, 783.99]

lengths = [0.125, 0.25, 0.5, 0.75, 1.00]

shortest = 0.1
short = 0.25
medium = 0.5
long = 0.75
longest = 1.0


def main():

    print("This is a simple program (randomly) generating music. What do you want to do?")

    command = ""

    while command != "exit":
        menu()
        command = input("Finished run. Type 'exit' to end the program or any other key to repeat.\n")

    print("Goodbye.")

    return


def menu():

    """
    the interface of the program
    """

    command = input("(1) play randomly generated melody (2) play 'the sound of bubble sort'\n")

    while command != "1" and command != "2":
        command = input("Command not found. Please enter '1' or '2'.\n")

    run_task(command)


def run_task(command):

    """
    support method for 'menu()'. Executes the function of the program according to user input

    :param command: command that the user entered in the menu
    """

    if command == "1":
        scale = get_scale_from_user()
        melodize(scale, duration=50)
        
    elif command == "2":
        array = generate_array(pentatonic_scale, 10)
        bubble_sort_auralized(pentatonic_scale, array, shortest)
    

def get_scale_from_user():

    """
    support method for the 'run_task()'. Retrieves the scale the user chooses

    :return: the scale the user chose
    """
    scale = input("Choose a scale: chromatic (all notes), blues or pentatonic (sounds nicest)!\n")

    while True:
        if scale == "chromatic":
            return chromatic_scale
        elif scale == "blues":
            return blues_scale
        elif scale == "pentatonic":
            return pentatonic_scale
        else:
            scale = input("Scale not found. Please enter 'chromatic', 'blues' or 'pentatonic'!\n")
        

def generate_array(scale, array_length):

    """
    support method, prepares the auralized bubble sort

    :param scale: determines the value range of the array (eg.: a pentatonic array has a smaller range than a blues one)
    :param array_length: length of array
    """

    array = []

    for i in range(array_length):
        array.append(random.randint(0, len(scale) - 1))

    return array


def melodize(scale, duration):

    """
    plays random notes with random length given scale and duration

    :param scale: scale that is used for the randomly generated music
    :param duration: how long randomly generated music is played
    """

    print("Melody is now playing.")

    for i in range(duration):

        tone_index = random.randint(0, len(scale) - 1)
        length_index = random.randint(0, len(lengths) - 1)

        sine(scale[tone_index], lengths[length_index])

        ''' attempt to make the music a bit nicer by introducing some regularity (it did not work)

        if tone_index >= len(scale) - 1:
            tone_index = 0

        if length_index >= len(lengths) - 1:
            length_index = 0

        sine(scale[tone_index + 1], lengths[length_index + 1])
        
        '''


def bubble_sort_auralized(scale, array, speed):

    """
    auralizes scale with given array at given speed

    :param scale: the scale out of which notes are chosen
    :param array: the array that represents the notes that are chosen
    :param speed: how fast the notes are played

    """

    print("The unsorted array is: " + str(array))

    n = len(array)

    # bubble sort
    for i in range(n):

        for j in range(0, n - i - 1):

            num1 = array[j]
            num2 = array[j + 1]

            if num1 > num2:
                array[j] = num2
                array[j + 1] = num1

            sine(scale[array[j]], speed)
            sine(scale[array[j]], speed)

            print("The current array is: " + str(array))

    print("The sorted array is: " + str(array))


def step(scale, step_size, speed, duration):

    """
    currently not in use
    steps through scale with given step_size, speed and duration

    :param scale: scale that is played
    :param step_size: interval within scale
    :param speed: how fast scale is played
    :param duration: how long the scale is looped through
    :return:
    """

    counter = 0

    for i in range(duration):

        sine(scale[counter], speed)
        counter += step_size

        if counter >= len(scale):
            counter -= len(scale)


if __name__ == "__main__":
    main()
