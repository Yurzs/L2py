import logging

import apscheduler.executors.asyncio
import apscheduler.jobstores.base
import apscheduler.jobstores.mongodb
import apscheduler.schedulers.asyncio

from common.application_modules.module import ApplicationModule
from common.document import Document

scheduler_job_store = {
    "default": apscheduler.jobstores.mongodb.MongoDBJobStore(
        client=Document.sync_client(), database="l2py"
    )
}
scheduler_executors = {"default": apscheduler.executors.asyncio.AsyncIOExecutor()}

scheduler = apscheduler.schedulers.asyncio.AsyncIOScheduler(
    jobstores=scheduler_job_store, executors=scheduler_executors
)


class ScheduleModule(ApplicationModule):
    _jobs = []

    def __init__(self):
        super().__init__("scheduler")
        self.scheduler = scheduler

    def start(self, config, loop):
        self.scheduler._eventloop = loop
        self.scheduler.start()
        self._add_jobs()
        logging.getLogger("apscheduler.executors.default").setLevel(logging.WARNING)

    def _add_jobs(self):
        for job in self._jobs:
            try:
                self.scheduler.add_job(job["f"], *job["args"], **job["kwargs"])
            except apscheduler.jobstores.base.ConflictingIdError:
                pass

    @classmethod
    def job(cls, *args, **kwargs):
        def wrap(f):
            kwargs.update({"name": f.__name__, "id": f.__name__})
            cls._jobs.append({"f": f, "args": args, "kwargs": kwargs})
            return f

        return wrap
