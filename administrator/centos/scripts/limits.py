import platform

if 'linux' in platform.system().lower():
    import resource  # Linux only

    limit_nofile = resource.getrlimit(resource.RLIMIT_NOFILE)
    limit_nproc = resource.getrlimit(resource.RLIMIT_NPROC)

    print ('Max number of opened files allowed:', limit_nofile)
    print ('Max number of processes allowed', limit_nproc)
