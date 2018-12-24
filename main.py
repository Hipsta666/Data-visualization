import matplotlib.pyplot as plt
import pylab


def course_dynamics(file):
    """The function builds a graph of the dynamics of a single currency."""
    list_data = []
    date = []
    days = 1
    with open(file) as data:
        for item in data:
            date.append(days)
            list_data.append(float(item))
            days += 1
    plt.title("Belarusian ruble (01/01/17 - 01/01/18)")
    plt.xlabel("Days")
    plt.ylabel("Course ")
    plt.grid(True)
    graph = input("Show the graph in standard form (1),"
                  " red lines (2), blue dots and lines (3): ")
    if graph == str(1):
        plt.plot(date, list_data)
        plt.show()
    if graph == str(2):
        plt.plot(date, list_data, 'r--')
        plt.show()
    if graph == str(3):
        plt.plot(date, list_data, '.-b')
        plt.show()
    else:
        print("Sorry, this kind of graphics can't be.")


def several_course_dynamics(file, graph):
    """The function builds graphs of the exchange
    rate of two currencies for comparison."""
    date = []
    course_USA = []
    course_CANADA = []
    days = 1
    with open(file) as data:
        text = data.readlines()
        for item in text:
            list_item = item.split()
            date.append(days)
            course_CANADA.append(float(list_item[1]))
            course_USA.append(float(list_item[0]))
            days += 1
    if graph == 2:
        plt.title("Dollar USA/Canada (01.01.16 - 30.06.2017)")
        plt.xlabel("Days")
        plt.ylabel("Course ")
        plt.grid(True)
        plt.plot(date, course_USA, date, course_CANADA)
        plt.show()
    if graph == 2.1:
        plt.figure(figsize=(10, 7))
        # subplot 1
        plt.subplot(221)
        plt.plot(date, course_USA)
        plt.title("Dollar USA")
        plt.grid(True)
        plt.xlabel("Days")
        plt.ylabel("Course ")
        # subplot 2
        plt.subplot(222)
        plt.plot(date, course_CANADA)
        plt.title("Canadian dollar")
        plt.grid(True)
        plt.xlabel("Days")
        plt.show()


def dynamic_chart(file):
    """The function builds a dynamic graph of
    changes in the currency exchange rate."""
    list_data = []
    date = []
    days = 1
    with open(file) as data:
        for item in data:
            date.append(days)
            list_data.append(float(item))
            days += 1
    pylab.ion()
    plt.title("Belarusian ruble (01/01/17 - 01/01/18)")
    plt.xlabel("Days")
    plt.ylabel("Course ")
    plt.grid(True)
    for n in range(date[-1]):
        pylab.plot(date[:n], list_data[:n], color="red")
        pylab.draw()
        pylab.pause(0.09)
    pylab.close()


def bar_chart(file):
    """The function builds histograms of the currency
    exchange rate of two or two currencies, depending on the user's choice."""
    date = []
    course_USA = []
    course_CANADA = []
    days = 1
    vocab_USA = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    vocab_CANADA = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    with open(file) as data:
        text = data.readlines()
        for item in text:
            list_item = item.split()
            date.append(days)
            if 1 <= days <= 31:
                vocab_USA[1] += float(list_item[0]) / 31
                vocab_CANADA[1] += float(list_item[1]) / 31
            if 32 <= days <= 59:
                vocab_USA[2] += float(list_item[0]) / 28
                vocab_CANADA[2] += float(list_item[1]) / 28
            if 60 <= days <= 90:
                vocab_USA[3] += float(list_item[0]) / 31
                vocab_CANADA[3] += float(list_item[1]) / 31
            if 91 <= days <= 120:
                vocab_USA[4] += float(list_item[0]) / 30
                vocab_CANADA[4] += float(list_item[1]) / 30
            if 121 <= days <= 151:
                vocab_USA[5] += float(list_item[0]) / 31
                vocab_CANADA[5] += float(list_item[1]) / 31
            if 152 <= days <= 181:
                vocab_USA[6] += float(list_item[0]) / 30
                vocab_CANADA[6] += float(list_item[1]) / 30
            if 182 <= days <= 212:
                vocab_USA[7] += float(list_item[0]) / 31
                vocab_CANADA[7] += float(list_item[1]) / 31
            if 213 <= days <= 243:
                vocab_USA[8] += float(list_item[0]) / 31
                vocab_CANADA[8] += float(list_item[1]) / 31
            if 244 <= days <= 273:
                vocab_USA[9] += float(list_item[0]) / 30
                vocab_CANADA[9] += float(list_item[1]) / 30
            if 274 <= days <= 304:
                vocab_USA[10] += float(list_item[0]) / 31
                vocab_CANADA[10] += float(list_item[1]) / 31
            if 305 <= days <= 334:
                vocab_USA[11] += float(list_item[0]) / 30
                vocab_CANADA[11] += float(list_item[1]) / 30
            if 335 <= days <= 365:
                vocab_USA[12] += float(list_item[0]) / 31
                vocab_CANADA[12] += float(list_item[1]) / 31
            days += 1
    for i in range(1, 13):
        course_CANADA.append(vocab_CANADA[i])
        course_USA.append(vocab_USA[i])
    graph = input("Show the histogram of the Canadian dollar (1), US dollar (2), both charts (3): ")
    plt.ylabel("Course ")
    plt.xlabel("Days")
    plt.grid(True)
    if graph == str(1):
        plt.title("Canadian dollar")
        plt.bar(date[:12], course_CANADA, align='center', alpha=0.5)
        plt.show()
    if graph == str(2):
        plt.title("Dollar USA")
        plt.bar(date[:12], course_USA, align='center', alpha=0.5)
        plt.show()
    if graph == str(3):
        plt.figure(figsize=(10, 7))
        # subplot 1
        plt.subplot(221)
        plt.bar(date[:12], course_USA, align='center', alpha=0.5)
        plt.title("Dollar USA")
        plt.xlabel("Days")
        plt.ylabel("Course ")
        # subplot 2
        plt.subplot(222)
        plt.bar(date[:12], course_CANADA, align='center', alpha=0.5)
        plt.title("Canadian dollar")
        plt.xlabel("Days")
        plt.show()
    else:
        print("Sorry, this kind of graphics can't be.")


def diagram():
    """The function builds a diagram of the volume of
     transactions for the purchase of US dollars and
     euros for rubles concluded by the Bank of Russia."""
    data = [157301, 94846.2, 62454.8]
    plt.figure(figsize=(10, 7))
    plt.title("Volume of transactions dollars and euros for rubles (01/17/17)")
    plt.pie(data, autopct='%.2f', labels=('Overall volume, million rubles(157301)',
                                          'EUR / RUB, million rubles(94846.2)',
                                          'USD / RUB, million rubles(62454.8)'))
    plt.show()


def main():
    """The function "communicates" with the user and displays graphs based on his desires."""
    print("""Single chart of the Belarusian ruble for 01/01/17 - 01/01/18 (1)
Dynamic schedule of the Belarusian ruble rate (1.1)
Two charts of the US dollar and the Canadian dollar 01/01/16 - 06/30/2017 (2) 
One exchange rate of the US dollar and the Canadian dollar (2.1)
Histogram of us dollar and canadian dollar (3)
Chart of the volume of transactions for the purchase of US dollars and euros for rubles on 01/17/2017 (4)""")
    print("What to show?")
    what_to_show = input()
    if what_to_show == str(1):
        course_dynamics("input.txt")
    if what_to_show == str(1.1):
        dynamic_chart("input.txt")
    if what_to_show == str(2):
        several_course_dynamics("output.txt", 2)
    if what_to_show == str(2.1):
        several_course_dynamics("output.txt", 2.1)
    if what_to_show == str(3):
        bar_chart("output.txt")
    if what_to_show == str(4):
        diagram()
    else:
        print("This is not listed")


if __name__ == '__main__':
    main()


