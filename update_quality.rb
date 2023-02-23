class Award
BLUE_FIRST = 'Blue First'
BLUE_COMPARE = 'Blue Compare'
BLUE_DISTINCTION_PLUS = 'Blue Distinction Plus'

attr_accessor :name, :expires_in, :quality

def initialize(name=nil, expires_in=nil, quality=nil)
@name = name
@expires_in = expires_in
@quality = quality
end

def update_quality
if @name != Award::BLUE_FIRST && @name != Award::BLUE_COMPARE
if @quality > 0
if @name != Award::BLUE_DISTINCTION_PLUS
@quality -= 1
end
end
else
if @quality < 50
@quality += 1
if @name == Award::BLUE_COMPARE
if @expires_in < 11
if @quality < 50
@quality += 1
end
end
if @expires_in < 6
if @quality < 50
@quality += 1
end
end
end

if @name != Award::BLUE_DISTINCTION_PLUS
  @expires_in -= 1
end

if @expires_in < 0
  if @name != Award::BLUE_FIRST
    if @name != Award::BLUE_COMPARE
      if @quality > 0
  
end
end
