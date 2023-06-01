import random
import csv

racers = ['Lewis', 'Valtteri', 'Max', 'Charles', 'Lando']
alg, lopp = 23, 26
times = []


def suvalineaeg(a, b):
    aeg = round(random.uniform(a, b), 3)
    return aeg


def format_time(sec):
    milliseconds = int((sec - int(sec)) * 1000)
    minutes, seconds = divmod(int(sec), 60)
    hours, minutes = divmod(minutes, 60)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}'


def taisringi_aeg():
    total = 0
    lap_times = []
    sector_times = []
    errors = []

    for lap in range(1, 11):
        s1 = suvalineaeg(alg, lopp)
        s2 = suvalineaeg(alg, lopp)
        s3 = suvalineaeg(alg, lopp)

        number = random.randint(1, 10)
        if number == 2:
            s1 = suvalineaeg(30, 90)
            s2 = suvalineaeg(30, 90)
            s3 = suvalineaeg(30, 90)
            errors.append("True")
        else:
            errors.append("False")

        lap_time = s1 + s2 + s3
        total += lap_time
        lap_times.append(lap_time)
        sector_times.append([s1, s2, s3])

    return total, lap_times, sector_times, errors


with open("Result.txt", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Ring", "Nimi", "Aeg", "Sektor1", "Sektor2", "Sektor3", "Viga"])

    for racer in racers:
        total_time, lap_times, sector_times, errors = taisringi_aeg()
        for i, (lap_time, sector, error) in enumerate(zip(lap_times, sector_times, errors), start=1):
            s1, s2, s3 = sector
            formatted_time = format_time(lap_time)
            writer.writerow([i, racer, formatted_time, s1, s2, s3, error])

print("Andmed on salvestatud CSV-faili 'Result.txt'.")
