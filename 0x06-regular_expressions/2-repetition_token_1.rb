#!/usr/bin/env ruby
# Matching our text string htn, hbtn

puts ARGV[0].scan(/hb{0,1}tn/).join

