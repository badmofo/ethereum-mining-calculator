# Ethereum Mining Calculator
View live version of [Ethereum Mining Calculator](https://badmofo.github.io/ethereum-mining-calculator/).

## Calculations

### Network hashrate 

We estimated the network hashrate in *GH* using the following equation.

```
netHashGH = (difficulty / blockTime) / 1e9;
```

Where `difficulty` is the current difficulty to mine a block and `blockTime` is the networks current block time.
