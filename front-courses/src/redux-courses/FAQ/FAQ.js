import {connect} from 'react-redux';
import {GET_FAQ} from './actions';

const stateFAQ = [
    {
        id: 1,
        question: 'Sint consequat mollit consequat irure exercitation ut in.',
        answer: 'In ut culpa irure laboris. Exercitation incididunt nostrud minim quis duis nostrud aute. Cupidatat veniam quis nisi ea laboris dolor et ea duis excepteur consectetur eu. Dolor dolor incididunt non ad. Nostrud aute aute proident proident anim duis velit in aliquip Lorem pariatur laboris ullamco. Veniam dolore labore irure proident. Aliquip id culpa ex officia aliquip.'
    },
    {
        id: 2,
        question: 'Sint consequat mollit consequat irure exercitation ut in.',
        answer: 'Sint cupidatat deserunt irure proident ex amet ad sit amet pariatur tempor culpa.'
    },
    {
        id: 3,
        question: 'Sint consequat mollit consequat irure exercitation ut in.',
        answer: 'Voluptate occaecat elit deserunt cupidatat quis cillum tempor ullamco ut. Do deserunt sit elit aute tempor amet ipsum officia et id do proident. Esse irure ipsum proident cupidatat duis veniam do est. Est sunt aliqua laboris dolor fugiat et labore velit quis cupidatat. Et aute nisi amet aliquip occaecat nostrud id id eu id Lorem. Exercitation do sint pariatur minim do exercitation aliqua eiusmod ipsum eu. Anim occaecat pariatur culpa tempor do occaecat elit et tempor consectetur. Dolore Lorem in do eiusmod sunt reprehenderit ut nisi duis. Ex magna do veniam cupidatat sint quis amet in ea cupidatat ipsum do excepteur. Mollit incididunt qui irure exercitation enim et est enim.'
    },
    {
        id: 4,
        question: 'Sint consequat mollit consequat irure exercitation ut in.',
        answer: 'In ut culpa irure laboris. Exercitation incididunt nostrud minim quis duis nostrud aute. Cupidatat veniam quis nisi ea laboris dolor et ea duis excepteur consectetur eu. Dolor dolor incididunt non ad. Nostrud aute aute proident proident anim duis velit in aliquip Lorem pariatur laboris ullamco. Veniam dolore labore irure proident. Aliquip id culpa ex officia aliquip.'
    },
    {
        id: 5,
        question: 'Sint consequat mollit consequat irure exercitation ut in.',
        answer: 'Sint cupidatat deserunt irure proident ex amet ad sit amet pariatur tempor culpa.'
    },
    {
        id: 6,
        question: 'Sint consequat mollit consequat irure exercitation ut in.',
        answer: 'Voluptate occaecat elit deserunt cupidatat quis cillum tempor ullamco ut. Do deserunt sit elit aute tempor amet ipsum officia et id do proident. Esse irure ipsum proident cupidatat duis veniam do est. Est sunt aliqua laboris dolor fugiat et labore velit quis cupidatat. Et aute nisi amet aliquip occaecat nostrud id id eu id Lorem. Exercitation do sint pariatur minim do exercitation aliqua eiusmod ipsum eu. Anim occaecat pariatur culpa tempor do occaecat elit et tempor consectetur. Dolore Lorem in do eiusmod sunt reprehenderit ut nisi duis. Ex magna do veniam cupidatat sint quis amet in ea cupidatat ipsum do excepteur. Mollit incididunt qui irure exercitation enim et est enim.'
    },
]

export default function reduserFAQ (FAQ=stateFAQ, action) {
    switch (action){
        case GET_FAQ:
            return FAQ
        default:
            return FAQ
    }
}