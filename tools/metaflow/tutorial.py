from metaflow import FlowSpec, step


class SampleFlow(FlowSpec):
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        print("SampleFlow is starting.")
        self.next(self.hello)

    @step
    def hello(self):
        """
        This is a middle step.
        """
        print("Metaflow says: Hi!")
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("SampleFlow is all done.")


if __name__ == '__main__':
    SampleFlow()
