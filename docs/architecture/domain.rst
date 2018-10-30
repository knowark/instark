Domain
------

Instark enables the delivery of **Messages** to a broad amount of **Devices**
that are subscribed to one or more **Channels**. These notifications may be
sent to an specific device or to all devices listening to a channel.


.. graphviz::

   digraph {
    graph [pad="0.5", nodesep="0.5", ranksep="2"];
    node [shape=plain]
    rankdir=LR;

    Device [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Device</i></td></tr>
    <tr><td port="id">id</td></tr>
    </table>>];

    Channel [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Channel</i></td></tr>
    <tr><td port="id">id</td></tr>
    </table>>];

    Subscription [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Subscription</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="device_id">device_id</td></tr>
    <tr><td port="channel_id">channel_id</td></tr>
    </table>>];

    Message [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td><i>Message</i></td></tr>
    <tr><td port="id">id</td></tr>
    <tr><td port="type">type: device | channel</td></tr>
    <tr><td port="reference">reference</td></tr>
    <tr><td port="content">content</td></tr>
    </table>>];

    Subscription:device_id -> Device:id;
    Subscription:channel_id -> Channel:id;

    }

