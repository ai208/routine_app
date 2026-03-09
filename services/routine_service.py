from datetime import date
class Routine_Service:
    def __init__(self,repository):
        self.repository = repository
    def complete_routine(self,routine):
        if not routine.done:
            routine.done = True
            routine.total_done += 1
            routine.last_done_date = date.today()

    def undo_routine(self,routine):
        if routine.done:
            routine.done = False
            routine.total_done -= 1
            routine.last_done_date = None
    def count_done(self):
        return sum(r.done for r in self.re) # r.done = True の時が1 だからこれを合計すればいい
    def count_total_task(self):
        return len(routine)