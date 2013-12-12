from PokerCalc import PokerCalc

d =2
p = 4
r = {'hand':25, 'base':8}
c = []

t = PokerCalc(decks = d, people = p, rules = r, out_cards = c, n=10000)
print 'removed the following cards'
print c
print 'using %s samples' % (str(t.get_sample_len()))

print 'probability of getting %s ' % (str([1,1,2,2]))
print t.get_player_sequence_probability([1,1,2,2])
print t.get_host_sequency_probability([1,1,2,2])


print 'probability of getting %s ' % (str([54,54]))
print t.get_player_sequence_probability([54,54])
print t.get_host_sequency_probability([54,54])

print 'probability of getting %s ' % (str([40]))
print t.get_player_sequence_probability([40])
print t.get_host_sequency_probability([40])