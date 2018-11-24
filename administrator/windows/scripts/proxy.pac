function FindProxyForURL(url, host)
{
  if (isPlainHostName(host)) {return "DIRECT";}
  if (shExpMatch(host, "127.0.0.1" )) {return "DIRECT";}
  if (shExpMatch(host, "*/localhost*" )) {return "DIRECT";}
  if (dnsDomainIs(host, ".***REMOVED***")) {return "DIRECT";}
  //if (!isInNet(host, "10.0.192.0", "	255.255.240.0")) {return "DIRECT";}  
  return "PROXY ***REMOVED***:3128";
}
