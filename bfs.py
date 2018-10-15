import queue

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def run(l: list):
    s = set(l)
    q = queue.Queue()
    res = []
    while s:
        p = s.pop()
        q.put(p)
        ss = [p]
        while not q.empty():
            p = q.get()
            for (x, y) in zip(dx, dy):
                nx, ny = x + p[0], y + p[1]
                if (nx, ny) in s:
                    q.put((nx, ny))
                    ss.append((nx, ny))
                    s.remove((nx, ny))
        if len(ss) > 10:
            res.append(ss)

    return res


if __name__ == '__main__':
    ll = [(462, 1510), (462, 1511), (463, 1509), (463, 1510), (463, 1511), (464, 1508), (464, 1509), (464, 1510), (465, 1506), (465, 1507), (465, 1508), (465, 1509), (466, 1505), (466, 1506), (466, 1507), (467, 1504), (467, 1505), (467, 1506), (468, 1503), (468, 1504), (468, 1505), (469, 1502), (469, 1503), (469, 1504), (470, 1500), (470, 1501), (470, 1502), (470, 1503), (471, 1499), (471, 1500), (471, 1501), (472, 1498), (472, 1499), (472, 1500), (473, 1498), (473, 1499), (474, 1498), (482, 1340), (483, 1340), (483, 1341), (483, 1342), (483, 1343), (484, 1340), (484, 1341), (484, 1342), (484, 1343), (484, 1344), (484, 1345), (485, 1343), (485, 1344), (485, 1345), (485, 1346), (485, 1347), (485, 1348), (486, 1346), (486, 1347), (486, 1348), (486, 1349), (486, 1350), (486, 1351), (487, 1349), (487, 1350), (487, 1351), (487, 1352), (487, 1353), (487, 1354), (488, 1352), (488, 1353), (488, 1354), (488, 1355), (488, 1356), (488, 1357), (489, 1355), (489, 1356), (489, 1357), (489, 1358), (489, 1359), (489, 1360), (490, 1357), (490, 1358), (490, 1359), (490, 1360), (490, 1361), (490, 1362), (490, 1363), (491, 1360), (491, 1361), (491, 1362), (491, 1363), (491, 1364), (491, 1365), (492, 1363), (492, 1364), (492, 1365), (492, 1366), (492, 1367), (492, 1368), (493, 1366), (493, 1367), (493, 1368), (493, 1369), (493, 1370), (493, 1371), (494, 1369), (494, 1370), (494, 1371), (494, 1372), (494, 1373), (494, 1374), (495, 1372), (495, 1373), (495, 1374), (495, 1375), (495, 1376), (495, 1377), (496, 1374), (496, 1375), (496, 1376), (496, 1377), (496, 1378), (496, 1379), (496, 1380), (497, 1377), (497, 1378), (497, 1379), (497, 1380), (497, 1381), (497, 1382), (498, 1380), (498, 1381), (498, 1382), (498, 1383), (503, 1454), (538, 1458), (538, 1459), (539, 1458), (539, 1459), (540, 1459), (540, 1460), (541, 1459), (541, 1460), (541, 1461), (542, 1460), (542, 1461), (542, 1462), (543, 1461), (543, 1462), (543, 1463), (544, 1462), (544, 1463), (545, 1463), (545, 1464), (546, 1463), (546, 1464), (546, 1465), (547, 1464), (547, 1465), (547, 1466), (548, 1465), (548, 1466), (548, 1467), (549, 1466), (549, 1467), (549, 1468), (550, 1467), (550, 1468), (551, 1468), (551, 1469), (552, 1468), (552, 1469), (552, 1470), (553, 1469), (553, 1470), (553, 1471), (554, 1470), (554, 1471), (554, 1472), (555, 1471), (555, 1472), (556, 1472), (556, 1473), (557, 1472), (557, 1473), (557, 1474), (558, 1473), (558, 1474), (558, 1475), (559, 1474), (559, 1475), (559, 1476)]
    print(len(run(ll)))