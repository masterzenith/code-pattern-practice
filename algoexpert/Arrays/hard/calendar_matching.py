"""
Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar and
your co-worker's calendar (both of which contain your respective meetings for the day, in the form of
[startTime, endTime]), as well as both of your daily bounds (i.e., the earliest and latest times at which you're
available for meetings every day, in the form of [earliestTime, latestTime]).
Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily
bounds, and the duration of the meeting that you want to schedule, and that returns a list of all the time blocks
(in the form of [startTime, endTime]) during which you could schedule the meeting, ordered from earliest time block to
latest.
Note that times will be given and should be returned in military time. For example: 8:30, 9:01, and 23:56.
Also note that the given calendar times will be sorted by start time in ascending order, as you would expect them to
appear in a calendar application like Google Calendar.

Sample Input:
calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

Sample Output:
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

Hints:
1. In order to find blocks of time during which you and your coworker can have a meeting, you have to first find all of
the unavailabilities between the two of you. An unavailability is any block of time during which at least one of you
is busy.
2. You'll have to start by taking into account the daily bounds; the daily bounds can be represented by two additional
meetings in each of your calendars.
3. Once you've taken the daily bounds into account, you'll want to merge the two calendars into a single calendar of
meetings and then flatten that calendar in order to eliminate overlapping and back-to-back meetings. This will give you
a calendar of unavailabilities, from which you can pretty easily find the list of matching availabilities.

Optimal Space & Time Complexity
O(c1 + c2) time | O(c1 + c2) space - where c1 and c2 are the respective numbers of meetings in calendar1 and calendar2
"""


def calendar_matching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration):
    updated_calendar1 = update_calendar(calendar1, daily_bounds1)
    updated_calendar2 = update_calendar(calendar2, daily_bounds2)
    merged_calendar = merge_calendars(updated_calendar1, updated_calendar2)
    flattened_calendar = flatten_calendar(merged_calendar)
    return get_matching_availabilities(flattened_calendar, meeting_duration)


def update_calendar(calendar, daily_bounds):
    updated_calendar = calendar[:]
    updated_calendar.insert(0, ["00:00", daily_bounds[0]])
    updated_calendar.append([daily_bounds[1], "23:59"])
    return list(map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], updated_calendar))


def merge_calendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged


def flatten_calendar(calendar):
    flattened = [calendar[0][:]]
    for i in range(1, len(calendar)):
        current_meeting = calendar[i]
        previous_meeting = flattened[-1]
        current_start, current_end = current_meeting
        previous_start, previous_end = previous_meeting
        if previous_end >= current_start:
            new_previous_meeting = [previous_start, max(previous_end, current_end)]
            flattened[-1] = new_previous_meeting
        else:
            flattened.append(current_meeting[:])
    return flattened


def get_matching_availabilities(calendar, meeting_duration):
    matching_availabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]
        end = calendar[i][0]
        availability_duration = end - start
        if availability_duration >= meeting_duration:
            matching_availabilities.append([start, end])
    return list(map(lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])], matching_availabilities))


def time_to_minutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


def minutes_to_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hours_string = str(hours)
    minutes_string = "0" + str(mins) if mins < 10 else str(mins)
    return hours_string + ":" + minutes_string


def main():
    calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    dailyBounds1 = ['9:00', '20:00']
    calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    dailyBounds2 = ['10:00', '18:30']
    meetingDuration = 30
    print(calendar_matching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))


if __name__ == "__main__":
    main()
