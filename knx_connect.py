import knx
import asyncio

# def connectKNX():


@knx.coroutine
def logger():
    while True:
        telegram = (yield)

    print('Telegram from {0} sent to {1} with value: {2}'.format(telegram.src, telegram.dst, telegram.value))


if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    coro = knx.bus_monitor(logger(), host='localhost', port=3671)
    loop.run_until_complete(coro)
