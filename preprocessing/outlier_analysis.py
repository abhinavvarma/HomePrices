

class DropRows():
    def drop(self, data, indices):
        indices.sort()
        adjust = 1
        for index in indices:
            data = data.drop(index - adjust, 0)
            temp = data[data["Id"] == index]
            assert temp.shape[0] == 0
            # adjust += 1
        return data

    def run(self, data):
        data = self.drop(data, [1299, 524, 582, 1191, 1062])
        return data