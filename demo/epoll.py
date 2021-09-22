import socket, select

svr_addr = ('0.0.0.0', 8888)

svn_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
svr_conn.bind(svr_addr)
svr_conn.listen(5)

epoll = select.epoll()
epoll.register(svr_conn.fileno(), select.EPOLLIN)
fd_to_conn = {svr_conn.fileno() : svr_conn}

while True:
    evts = epoll.poll(-1)
    if evts:
        for fd, evt in evts:
            conn = fd_to_conn[fd]
            if conn == svr_conn:
                clt_conn, addr = svr_conn.accpet()
                epoll.register(clt_conn.fileno(), select.EPOLLIN)
                fd_to_conn[clt_conn.fileno()] = clt_conn
            elif evt & select.EPOLLHUP:
                epoll.unregister(fd)
                fd_to_conn[fd].close()
                del fd_to_conn[fd]
                del fd_to_buf[fd]
            elif evt & select.EPOLLIN:
                data = conn.recv(65536)
                if data:
                    # ...
                    epoll.modify(fd, select.EPOLLOUT)
            elif evt & select.EPOLLOUT:
                #...
                epoll.modify(fd, select.EPOLLIN)
