#!/usr/bin/env ruby
# Matches the regular expression School

puts (ARGV[0] || "").scan(/School/).join
