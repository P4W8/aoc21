d = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

p1 = minimum([sum(abs.(d .- i)) for i = 0:maximum(d)])
intsum(x) = (x * (x + 1)) / 2
p2 = minimum([sum(intsum.(abs.(d .- i))) for i = 0:maximum(d)])

println("Part 1: $(Int(p1)) || Part 2: $(Int(p2))")