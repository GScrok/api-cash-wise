from finance_control_service.application.goals.goals_storage import GoalStorage
from finance_control_service.application.goals.goals_dto import GoalDTO
from finance_control.models import Category, User, Goal

from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist


class GoalRepository(GoalStorage):
    def _dto_to_model(self, goal_dto: GoalDTO) -> Goal:
        try:
            user = User.objects.get(pk=goal_dto.user_id)
            category = None
            if goal_dto.category_id:
                category = Category.objects.get(pk=goal_dto.category_id)
        except ObjectDoesNotExist as e:
            raise ValueError(f"Invalid related object: {e}")
        
        goal = Goal(
            id=goal_dto.id,
            name=goal_dto.name,
            user=user,
            category=category,
            value=goal_dto.value,
            description=goal_dto.description,
            start_at=goal_dto.start_at,
            end_at=goal_dto.end_at,
        )
        return goal

    def _model_to_dto(self, goal: Goal) -> GoalDTO:
        return GoalDTO({
            "id": goal.id,
            "name": goal.name,
            "user_id": goal.user.id,
            "category_id": goal.category.id if goal.category else None,
            "value": goal.value,
            "description": goal.description,
            "start_at": goal.start_at,
            "end_at": goal.end_at,
        })

    def verify_existing_by_name(self, goal_dto: GoalDTO) -> bool:
        return Goal.objects.filter(
            name=goal_dto.name,
            category_id=goal_dto.category_id,
        ).exists()

    def verify_existing_by_name_exclude_current(self, goal_dto: GoalDTO, pk: UUID) -> bool:
        return Goal.objects.filter(
            name=goal_dto.name,
            category_id=goal_dto.category_id,
        ).exclude(pk=pk).exists()

    def get_by_id(self, id: UUID) -> GoalDTO:
        try:
            goal = Goal.objects.get(pk=id)
            return self._model_to_dto(goal)
        except Goal.DoesNotExist:
            raise ValueError("Goal not found.")

    def get_all(self) -> list[GoalDTO]:
        return [self._model_to_dto(goal) for goal in Goal.objects.all()]

    def get_all_by_category(self, category_id: UUID) -> list[GoalDTO]:
        return [self._model_to_dto(goal) for goal in Goal.objects.filter(category_id=category_id)]

    def get_all_by_user(self, user_id: UUID) -> list[GoalDTO]:
        return [self._model_to_dto(goal) for goal in Goal.objects.filter(user_id=user_id)]

    def save(self, goal_dto: GoalDTO) -> GoalDTO:
        goal = self._dto_to_model(goal_dto)
        goal.save()
        return self._model_to_dto(goal)

    def update(self, goal_dto: GoalDTO) -> GoalDTO:
        try:
            goal = Goal.objects.get(pk=goal_dto.id)
            updated_goal = self._dto_to_model(goal_dto)
            for field, value in updated_goal.__dict__.items():
                setattr(goal, field, value)
            goal.save()
            return self._model_to_dto(goal)
        except Goal.DoesNotExist:
            raise ValueError("Goal not found.")

    def delete(self, id: UUID) -> bool:
        try:
            goal = Goal.objects.get(pk=id)
            goal.delete()
            return True
        except Goal.DoesNotExist:
            raise ValueError("Goal not found.")
