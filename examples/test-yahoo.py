from search_engine_tool_vito1317 import yahoo


def test_yahoo():
    try:
        data = yahoo.search("台灣天氣")
        for d in data:
            print(d)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_yahoo()