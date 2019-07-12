package bi.zum.lab3;

import cz.cvut.fit.zum.api.ga.AbstractEvolution;
import cz.cvut.fit.zum.api.ga.AbstractIndividual;
import cz.cvut.fit.zum.data.Edge;
import cz.cvut.fit.zum.data.StateSpace;
import cz.cvut.fit.zum.util.Pair;

import java.util.List;
import java.util.Random;

/**
 * @author Your Name
 */
public class Individual extends AbstractIndividual {

    private double fitness = Double.NaN;
    private AbstractEvolution evolution;

    // @TODO Declare your genotype
    boolean[] genome;


    /**
     * Creates a new individual
     *
     * @param evolution The evolution object
     * @param randomInit <code>true</code> if the individial should be
     * initialized randomly (we do wish to initialize if we copy the individual)
     */
    public Individual(AbstractEvolution evolution, boolean randomInit) {
        this.evolution = evolution;
        int size = evolution.getNodesCount();
        this.genome = new boolean[size];
        Random rand = new Random();

        if(randomInit) {
            for (int i = 0; i<size;i++)
            {
                genome[i] = rand.nextBoolean();

            }
            // @TODO initialize individual
            repair();
        }
//        computeFitness();
    }

    @Override
    public boolean isNodeSelected(int j) {


        // @TODO Implement based on your individual's genotype
        return genome[j];


//        return false;
    }

    /**
     * Evaluate the value of the fitness function for the individual. After
     * the fitness is computed, the <code>getFitness</code> may be called
     * repeatedly, saving computation time.
     */
    @Override
    public void computeFitness() {


        // @TODO: Implement fitness based on your implementation
        // Hint: use the StateSpace object
//        StateSpace.edgesCount();
//        Node a = StateSpace.getNode(1);
//        Edge b = StateSpace.getEdge(1);

        double base = StateSpace.nodesCount();

        for (int i = 0;i<this.genome.length;i++)
            if (genome[i])
                base--;

//        int penalization = 1;
//
//        List<Edge> edges = StateSpace.getEdges();
//        for (Edge e:edges) {
//            if ( ! genome[e.getFromId()] && ! genome[e.getToId()] )
//                penalization++;
//
//        }
//
//        base = base/penalization;



        this.fitness = base;
    }

    /**
     * Only return the computed fitness value
     *
     * @return value of fitness fucntion
     */
    @Override
    public double getFitness() {
        return this.fitness;
    }

    /**
     * Does random changes in the individual's genotype, taking mutation
     * probability into account.
     *
     * @param mutationRate Probability of a bit being inverted, i.e. a node
     * being added to/removed from the vertex cover.
     */
    @Override
    public void mutate(double mutationRate) {

        Random rand = new Random();
        for(int i=0; i<this.genome.length; i++) {
            if(rand.nextDouble() < mutationRate) {
                this.genome[i] = !this.genome[i];
            }
        }

        this.repair();

    }

    /**
     * Crosses the current individual over with other individual given as a
     * parameter, yielding a pair of offsprings.
     *
     * @param other The other individual to be crossed over with
     * @return A couple of offspring individuals
     */
    @Override
    public Pair crossover(AbstractIndividual other) {

        Pair<Individual,Individual> result = new Pair();
        Random rand = new Random();
        int crossPoint = rand.nextInt(genome.length);

        Individual inA = new Individual(evolution,false);
        Individual inB = new Individual(evolution,false);

        boolean[] newGenA = new boolean[genome.length];
        boolean[] newGenB = new boolean[genome.length];
//        first half
        for (int i = 0; i<crossPoint ;i++)
        {
            newGenA[i] = other.isNodeSelected(i);
            newGenB[i] = genome[i];
        }
//        second half
        for (int i = crossPoint; i<genome.length;i++)
        {
            newGenA[i] = genome[i];
            newGenB[i] = other.isNodeSelected(i);
        }

        inA.genome = newGenA;
        inB.genome = newGenB;
        inA.repair();
        inB.repair();
        // @TODO implement your own crossover
        result.a = inA;
        result.b = inB;

        return result;
    }

    /**
     * When you are changing an individual (eg. at crossover) you probably don't
     * want to affect the old one (you don't want to destruct it). So you have
     * to implement "deep copy" of this object.
     *
     * @return identical individual
     */
    @Override
    public Individual deepCopy() {
        Individual newOne = new Individual(evolution, false);

        System.arraycopy(this.genome, 0, newOne.genome, 0, this.genome.length);

        // TODO: at least you should copy your representation of search-space state

        newOne.fitness = this.fitness;
        return newOne;
    }

    /**
     * Return a string representation of the individual.
     *
     * @return The string representing this object.
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();


        /* TODO: implement own string representation, such as a comma-separated
         * list of indices of nodes in the vertex cover
         */


        sb.append(super.toString());

        return sb.toString();
    }

    public void repair(){
        List<Edge> edges = StateSpace.getEdges();
        for (Edge e:edges) {
            if (!genome[e.getFromId()] && !genome[e.getToId()]) {
                Random rand = new Random();
                boolean from = rand.nextBoolean();
                if (from)
                    genome[e.getFromId()] = true;
                else
                    genome[e.getToId()] = true;
            }
        }
    }
}