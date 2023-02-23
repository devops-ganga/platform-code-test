def __init__(self, name=None, expires_in=None, quality=None):
    self.name = name
    self.expires_in = expires_in
    self.quality = quality

def update_quality(self):
    if self.name != Award.BLUE_FIRST and self.name != Award.BLUE_COMPARE:
        if self.quality > 0:
            if self.name != Award.BLUE_DISTINCTION_PLUS:
                self.quality -= 1
    else:
        if self.quality < 50:
            self.quality += 1
            if self.name == Award.BLUE_COMPARE:
                if self.expires_in < 11:
                    if self.quality < 50:
                        self.quality += 1
                if self.expires_in < 6:
                    if self.quality < 50:
                        self.quality += 1

    if self.name != Award.BLUE_DISTINCTION_PLUS:
        self.expires_in -= 1

    if self.expires_in < 0:
        if self.name != Award.BLUE_FIRST:
            if self.name != Award.BLUE_COMPARE:
                if self.quality > 0:
                    if self.name != Award.BLUE_DISTINCTION_PLUS:
                        self.quality -= 1
            else:
                self.quality = 0
        else:
            if self.quality < 50:
                self.quality += 1
