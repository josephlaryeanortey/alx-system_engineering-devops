Here's a README format for your web stack debugging task:

---

# Web Stack Debugging Task

## Overview

This task involves testing and optimizing a web server setup using Nginx to handle a high volume of requests. We use ApacheBench to benchmark the server's performance under pressure and make necessary adjustments to achieve optimal results.

## Objective

The goal is to ensure that our web server can handle a high number of requests efficiently. We aim to eliminate failed requests and improve performance by configuring Nginx and applying Puppet to manage settings.

## Benchmarking

We used ApacheBench (ab) to simulate HTTP requests to the web server. The benchmarking command used is:

```bash
ab -c 100 -n 2000 localhost/
```

This command sends 2000 requests to the server with a concurrency level of 100.

### Initial Results

Before applying any fixes, the benchmark results showed:

- **Server Software**: nginx/1.4.6
- **Server Hostname**: localhost
- **Server Port**: 80
- **Document Path**: /
- **Document Length**: 201 bytes
- **Concurrency Level**: 100
- **Time taken for tests**: 0.353 seconds
- **Complete requests**: 2000
- **Failed requests**: 943 (Length: 943)
- **Non-2xx responses**: 1057
- **Requests per second**: 5664.01 [#/sec] (mean)
- **Time per request**: 17.655 ms (mean)
- **Transfer rate**: 3309.15 Kbytes/sec received

### Action Taken

We applied a Puppet configuration to address the issues with the web server setup. The Puppet file used is `0-the_sky_is_the_limit_not.pp`.

```bash
sudo puppet apply 0-the_sky_is_the_limit_not.pp
```

### Post-Fix Results

After applying the Puppet configuration, the benchmark results improved significantly:

- **Server Software**: nginx/1.4.6
- **Server Hostname**: localhost
- **Server Port**: 80
- **Document Path**: /
- **Document Length**: 612 bytes
- **Concurrency Level**: 100
- **Time taken for tests**: 0.301 seconds
- **Complete requests**: 2000
- **Failed requests**: 0
- **Total transferred**: 1706000 bytes
- **HTML transferred**: 1224000 bytes
- **Requests per second**: 6650.99 [#/sec] (mean)
- **Time per request**: 15.035 ms (mean)
- **Transfer rate**: 5540.33 Kbytes/sec received

### Connection Times

- **Connect**: Min: 0 ms, Mean: 4 ms, Median: 3 ms, Max: 12 ms
- **Processing**: Min: 2 ms, Mean: 11 ms, Median: 10 ms, Max: 31 ms
- **Waiting**: Min: 1 ms, Mean: 10 ms, Median: 8 ms, Max: 29 ms
- **Total**: Min: 5 ms, Mean: 15 ms, Median: 14 ms, Max: 31 ms

### Response Time Percentiles

- **50%**: 14 ms
- **66%**: 17 ms
- **75%**: 18 ms
- **80%**: 19 ms
- **90%**: 22 ms
- **95%**: 26 ms
- **98%**: 27 ms
- **99%**: 28 ms
- **100%**: 31 ms (longest request)

## Repository

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/josephlaryeanortey/alx-system_engineering-devops)
- **Directory**: 0x1B-web_stack_debugging_4
- **File**: 0-the_sky_is_the_limit_not.pp
