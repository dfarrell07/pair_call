## Pair Call Generator

Tool that pairs off devs for a daily stand-up call.

### Usage

If you're not on my dev team, you'll want to fork the codebase and modify the `Pair.devs` list to contain the names of the devs on your team. You can then have them clone your fork, after which you'll be good to go. If the `Pair.devs` list or the `Pair.start_day` date changes, make sure everyone pulls the update. Else, they will get different pairs for a given day.

If you're on my team, just pull the code and run it as shown below.

```
[~/pair_call]$ ./pair.py
Your name: Daniel
You're paired with: Madhu
[~/pair_call]$ ./pair.py
Your name: Madhu 
You're paired with: Daniel
```

Note that invalid devs will produce the following output, including the list of known devs.

```
[~/pair_call]$ ./pair.py
Your name: not_a_dev
Unknown dev: not_a_dev, known devs: ['Sam', 'Chris', 'Dave', 'Madhu', 'Brent', 'Flavio', 'Daniel', 'Day off']
```

The name input part of the code isn't case sensitive.

```
[~/pair_call]$ ./pair.py
Your name: daniel
You're paired with: Madhu
```

### Contributing

Contributions are welcome!

For bugs or feature requests, please raise an [Issue](https://github.com/dfarrell07/pair_call/issues) via GitHub.

To contribute changes, fork the code base, make your changes and then submit a pull request.

You can contact me directly at dfarrell@redhat.com or on IRC at Freenode/#opendaylight. My nic is dfarrell07.
