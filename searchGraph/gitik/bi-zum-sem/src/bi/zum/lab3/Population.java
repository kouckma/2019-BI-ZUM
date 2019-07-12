package bi.zum.lab3;

import cz.cvut.fit.zum.api.ga.AbstractEvolution;
import cz.cvut.fit.zum.api.ga.AbstractIndividual;
import cz.cvut.fit.zum.api.ga.AbstractPopulation;
import cz.cvut.fit.zum.data.StateSpace;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * @author Your name
 */
public class Population extends AbstractPopulation {

    Random random = new Random();
    public Population(AbstractEvolution evolution, int size) {
        individuals = new Individual[size];
        for (int i = 0; i < individuals.length; i++) {
            individuals[i] = new Individual(evolution, true);
            individuals[i].computeFitness();
        }
    }

    /**
     * Method to select individuals from population
     *
     * @param count The number of individuals to be selected
     * @return List of selected individuals
     */
    public List<AbstractIndividual> selectIndividuals(int count) {
        ArrayList<AbstractIndividual> selected = new ArrayList<AbstractIndividual>();
        for (int i=0; i<count;i++)
        {
            double bestF = Double.NEGATIVE_INFINITY;
            AbstractIndividual bestI = null;
            for (int j = 0;j<100;j++)
            {
                AbstractIndividual recruit = this.individuals[random.nextInt(this.individuals.length)];
                if (recruit.getFitness() > bestF)
                {
                    bestI = recruit;
                    bestF = recruit.getFitness();
                }
            }
            selected.add(bestI);
        }
        return selected;
    }

}
