from multiprocessing import Process, Value
from typing import Optional, List


class Service:
    def __init__(self, name):
        self.name = name


class RoundRobin:
    def __init__(self, counter: Value):
        self.counter = counter
        self.services: List[Service] = []

    def add_service(self, name):
        self.services.append(Service(name))

    def get_next_service(self) -> Optional[Service]:
        with self.counter.get_lock():
            service: Service = self.services[self.counter.value]
            if self.counter.value == len(self.services) - 1:
                self.counter.value = 0
            else:
                self.counter.value += 1
            return service


def run_job(rr: RoundRobin):
    for _ in range(10):
        print(rr.get_next_service().name)


if __name__ == "__main__":
    c = Value('i', 0)
    rr = RoundRobin(c)
    rr.add_service("service1")
    rr.add_service("service2")
    rr.add_service("service3")
    rr.add_service("service4")

    jobs = []
    for i in range(3):
        process = Process(target=run_job, args=(rr,))
        jobs.append(process)
    for i in jobs:
        i.start()
    for i in jobs:
        i.join()
