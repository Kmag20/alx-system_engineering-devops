#!/usr/bin/env ruby
# Matches log provided

puts ARGV[0].scan(/\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/).join(",")
