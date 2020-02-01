# WeeWX-exporter
A custom metric exporter for WeeWX in [Prometheus](https://prometheus.io/) format 

This is a custom exported written in Python to provide access to realtime metrics from a weather station running on [WeeWX](http://www.weewx.com/). It does this by scraping the `realtime.txt` file that is made avaialbe via the [Cumulus Real Time](https://github.com/weewx/weewx/wiki/crt) (crt) extention.

The exporter makes the data available in the [Prometheus](https://prometheus.io/) format so that it can be used to feed into follow on tools such as [Grafana](https://grafana.com/).

A general guide for installing a custom exporter can be found [here](https://leanpub.com/rpcmonitor/read#leanpub-auto-custom-exporters).
