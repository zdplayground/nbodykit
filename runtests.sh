cd examples
bash get-data.sh || exit 1
bash fof/run.sh || exit 1
bash power/run.sh || exit 1
bash subhalo/run.sh || exit 1
bash trace-halo/run.sh || exit 1
