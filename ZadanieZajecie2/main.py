import Processor


def main():
    processor = Processor.Processor()
    processor.initForm()
    processor.initControls()
    processor.drawPlot()
    processor.initLoop()


if __name__ == "__main__":
        main()
