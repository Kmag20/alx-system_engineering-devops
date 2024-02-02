#!/usr/bin/env ruby
# Matches a string that starts with h and ends with n with a single character 
# between them

puts ARGV[0].scan(/h.n/).join
