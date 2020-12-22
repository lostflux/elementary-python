from counter import Counter

class Timer:
    def _init_(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.t_hr = Counter(24, initial = self.hours, min_digits = 2)
        self.t_min = Counter(60, initial=self.minutes, min_digits = 2)
        self.t_sec = Counter(60, initial=self.seconds, min_digits = 2)

    def is_zero(self):
        if str(self) == "00:00:00":
            return True
        return False

    def _str_(self):

        # # if self.hours / 10 < 1:
        #     hr = "0" + str(self.hours)
        # else:
        #     hr = str(self.hours)
        #
        # if self.minutes / 10 < 1:
        #     min = "0" + str(self.minutes)
        # else:
        #     min = str(self.minutes)
        #
        # if self.seconds / 10 < 1:
        #     sec = "0" + str(self.seconds)
        # else:
        #     sec = str(self.seconds)

        return str(self.t_hr)+":"+str(self.t_min)+":"+str(self.t_sec)


    def tick(self):
        if self.t_sec.tick():
            if self.t_min.tick():
                self.t_hr.tick()
