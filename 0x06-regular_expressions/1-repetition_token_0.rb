#!/usr/bin/env ruby
# Matches the repetition of letter t as our example

puts (ARGV[0]).scan(/hbt{2,5}n/).join
